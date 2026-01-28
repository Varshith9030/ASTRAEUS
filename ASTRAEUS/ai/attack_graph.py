from graphviz import Digraph

def build_attack_graph(findings, output_file="attack_path"):
    graph = Digraph(comment="Attack Path Graph", format="png")
    graph.attr(rankdir="LR", size="8,5")

    nodes = {}
    edges = []

    for f in findings:
        title = f["title"]
        severity = f.get("severity", "LOW")

        color = severity_color(severity)
        node_id = normalize(title)

        nodes[node_id] = title
        graph.node(node_id, title, style="filled", fillcolor=color)

        chain = f.get("attack_chain")
        if chain:
            steps = [s.strip() for s in chain.split("→")]
            for i in range(len(steps) - 1):
                src = normalize(steps[i])
                dst = normalize(steps[i + 1])
                graph.node(src, steps[i])
                graph.node(dst, steps[i + 1])
                edges.append((src, dst))

    for src, dst in edges:
        graph.edge(src, dst)

    graph.render(output_file, cleanup=True)
    return output_file + ".png"


def severity_color(severity):
    return {
        "CRITICAL": "red",
        "HIGH": "orange",
        "MEDIUM": "yellow",
        "LOW": "lightgrey"
    }.get(severity, "white")


def normalize(text):
    return text.lower().replace(" ", "_").replace("-", "_")
