# 📘 study-monorepo-onlinesalon

オンラインサロンの会員管理やWebサービス機能を、**モノレポ構成**（Turborepo + pnpm workspace）で構築・学習するプロジェクトです。  
**Next.js + FastAPI + OpenAPI（型共有）** を用いたモダンなWebアプリ開発の実践環境です。

---

## 🧩 技術スタック

| 区分           | 使用技術                        |
|----------------|---------------------------------|
| フロントエンド | Next.js (TypeScript, React)     |
| バックエンド   | FastAPI (Python)                |
| API仕様管理    | OpenAPI                         |
| モノレポ管理   | Turborepo + pnpm workspace      |

---

## 📁 ディレクトリ構成

```
study-monorepo-onlinesalon/
├── apps/
│   ├── web/               # Next.js フロントエンドアプリ
│   └── api/               # FastAPI バックエンドアプリ
├── packages/
│   └── shared-types/      # OpenAPIから生成された型定義
├── openapi/               # OpenAPI スキーマファイル（YAML/JSON）
├── turbo.json             # Turborepo 設定
├── pnpm-workspace.yaml    # pnpm workspace 設定
└── README.md              # このファイル
```

---

## 🚀 初期セットアップ手順

### 1. リポジトリをクローン

```bash
git clone https://github.com/your-username/study-monorepo-onlinesalon.git
cd study-monorepo-onlinesalon
```
2. 依存パッケージをインストール
```bash
pnpm install
```
3. アプリを起動
```bash
# 開発用に Turbo 経由で両アプリ起動
pnpm dev
```

---

## 📌 今後の予定（ToDo）
- `apps/web` に **Next.js プロジェクト** を追加  
- `apps/api` に **FastAPI プロジェクト** を追加  
- `openapi/` にスキーマを記述し、型を `shared-types/` に生成  
- **CI/CD 連携**（例: GitHub Actions など）  
- **デプロイ**（例: Vercel / Railway / Render などを想定）