up:        ; docker compose up --build
migrate:   ; docker compose exec api alembic upgrade head
revision:  ; docker compose exec api alembic revision --autogenerate -m "$(m)"
test:      ; docker compose exec api pytest -q
lint:      ; docker compose exec api sh -c "ruff check . && mypy app"
eval:      ; docker compose exec -w / api python -m eval.run --config eval/configs/$(c).yaml
