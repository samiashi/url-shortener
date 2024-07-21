# url shortener

Was bored on a plane so built this url shortener concept. Nothing special really.

Setup Python
```bash
uv venv --python ~/.pyenv/versions/3.11.9/bin/python
source .venv/bin/activate
uv pip install -r requirements.txt
```

Then start the Django server
```bash
python manage.py migrate
python manage.py runserver
```

### Test

Generate a shortened url for `http://localhost:8000/admin/url_shortener/redirect/`. (Had no access to the internet so was redirecting to django admin)
```bash
curl 
    -X POST 
    http://localhost:8000/generate/ 
    -d '{"url": "http://localhost:8000/admin/url_shortener/redirect/"}'
```

Which will return the shortened url -> `http://localhost:8000/a05fdab4`

We will track the number of hits this shortened url gets and the last hit date.
