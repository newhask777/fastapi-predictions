html = """
<script>
var ws = new Websocket("wc://localhost:8000/live);
ws.onmessage = function(event){
console.log(ws);
}

<script>
"""