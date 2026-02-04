def get_diagram(diagram_type, data):
    if diagram_type == "right_triangle":
        return {
            "type": "svg",
            "content": f"""
            <svg width="200" height="150">
              <polygon points="20,120 180,120 20,20"
                       style="fill:none;stroke:black;stroke-width:2"/>
              <text x="40" y="115">{data['a']}cm</text>
              <text x="100" y="70">{data['b']}cm</text>
            </svg>
            """
        }
