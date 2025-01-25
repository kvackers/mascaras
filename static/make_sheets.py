import json

with open("static/class.json", 'r') as file:
    data = json.load(file)

with open("static/template-ficha.html") as file:
    template = file.read()

for klass, dicts in data.items():
    fulfilled = template
    
    for key, value in dicts.items():
        if isinstance(value, str):
            fulfilled = fulfilled.replace(key, value)
        elif isinstance(value, int):
            fulfilled = fulfilled.replace(key, str(value))
        elif key == "#BACKSTORY#":
            replacer = "".join([f"<li>{item}</li>" for item in value])
            fulfilled = fulfilled.replace(key, replacer)
        elif key.startswith("#ADVANCEMENT") or key in ["#EXTRA-LIST#", "#HABILIDADES#", "#MOVES#"]:
            pre_input = "" if key == "#EXTRA-LIST#" and dicts.get("extranocheck", False) else "<input type=\"checkbox\">"
            replacer = "".join([f"<li>{pre_input}{item}</li>" for item in value])
            fulfilled = fulfilled.replace(key, replacer)
        elif key == "#APARENCIA#":
            replacer = "".join([
                "<li>" + 
                ", ".join([f"<span class=\"choosey\">{item}</span>" for item in sublist]) + 
                "</li>" 
                for sublist in value
            ])
            fulfilled = fulfilled.replace(key, replacer)
    
    with open(f"static/ficha-{klass}.html", "w") as file:
        file.write(fulfilled)