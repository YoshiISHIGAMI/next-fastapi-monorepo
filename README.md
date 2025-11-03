# 📦 next-fastapi-monorepo

## 📝 概要（Overview in Japanese）

このリポジトリは、**Next.js（TypeScript）** と **FastAPI（Python）** を組み合わせて構築された、モダンな**モノレポ開発環境のテンプレート**です。  
APIスキーマには **OpenAPI** を用い、`shared-types` ディレクトリでフロントエンドとバックエンドの**型を共有**します。

## 🛠 技術スタック

| 区分           | 使用技術                                        |
|----------------|-------------------------------------------------|
| フロントエンド | Next.js, TypeScript, Tailwind CSS              |
| バックエンド   | FastAPI, Python, Poetry                         |
| APIドキュメント | Swagger UI / Redoc (via FastAPI)               |
| 型共有         | OpenAPI → `shared-types`（自動生成）           |
| モノレポ管理   | Turborepo + pnpm workspace                      |

---

## ⚙️ 開発環境のセットアップ

このプロジェクトは **pnpm + Turborepo + Poetry** を使用しています。  
初回クローン後は以下の手順でセットアップしてください。

---

### 🧩 前提条件

| ツール | バージョン | 備考 |
|--------|-------------|------|
| Node.js | 22.x | Volta や asdf で固定推奨 |
| pnpm | 10.x 以上 | `npm install -g pnpm` |
| Python | 3.12.x | asdf / pyenv / system いずれでも可 |
| Poetry | 2.2.x | `pip install poetry` or `curl -sSL https://install.python-poetry.org | python3 -` |

---

### 📦 依存パッケージのインストール

#### 1. ルートで JavaScript パッケージをインストール

```bash
pnpm install
```

#### 2. FastAPI 側の依存を Poetry でインストール

```bash
cd apps/api
poetry install
```
poetry install は pyproject.toml に基づき仮想環境を自動作成します。

⸻

### 🚀 開発サーバーの起動

#### Next.js (frontend)

```bash
cd apps/web
pnpm dev
```

アクセス: http://localhost:3000￼

#### FastAPI (backend)

```bash
cd apps/api
poetry run uvicorn api.main:app --reload
```

アクセス: http://127.0.0.1:8000/docs￼（Swagger UI）

⸻

### 🧠 よく使うコマンド

| コマンド | 用途 |
|---------|------|
| `pnpm dev` | Next.js 開発サーバー起動 |
| `pnpm lint` | Lint チェック |
| `pnpm format` | コード整形 |
| `poetry run uvicorn api.main:app --reload` | FastAPI 起動 |
| `npx openapi-typescript openapi/schema.yaml --output packages/shared-types/api-types.ts` | OpenAPI から TypeScript 型を自動生成 |


⸻

### 📁 プロジェクト構成（抜粋）

```
apps/
  ├── web/     # Next.js
  └── api/     # FastAPI
openapi/
  └── schema.yaml
packages/
  └── shared-types/
docs/
  └── TODO.md
```

---

## 🧭 Project Roadmap

> ✅ **目的:** 将来「クローンして即動かす」ことができる。

See [`docs/TODO.md`](./docs/TODO.md) for the current development roadmap.