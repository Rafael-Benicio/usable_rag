
### Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Executar

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 3000 --reload

```

### Test

Cole no terminal a função

```bash

postTest(){
	echo '';

	curl -d $1 -H "Content-Type: application/json" -X POST $2;
	
	echo '';
}
```

#### Obtendo documentos

```bash
postTest "{\"query\":\"liquidez\"}" "http://127.0.0.1:3000/query"

postTest "{\"query\":\"licença moral\"}" "http://127.0.0.1:3000/query" 

postTest "{\"query\":\"competitividade\"}" "http://127.0.0.1:3000/query"
```