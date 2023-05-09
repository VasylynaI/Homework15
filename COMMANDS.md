1. Усі тести з мітками "from_class" та "pack":
pytest -m "from_class or pack"

2. Усі тести з усіма мітками крім "from_class":
pytest -m "not from_class"

3. Усі тести з мітками "pack" але виключити тести з міткою "rest":
pytest -m "pack and not rest"