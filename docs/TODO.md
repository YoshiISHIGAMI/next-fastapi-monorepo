# 🛠️ next-fastapi-monorepo - 開発タスク一覧

## ✅ 完了済
- [x] apps/web に Next.js プロジェクトを作成
- [x] apps/api に FastAPI プロジェクトを作成
- [x] モノレポ構成を整備（pnpm workspace + turborepo）

## 📌 進行中 or 今後のタスク

### 📐 型定義・OpenAPI連携
- [ ] `openapi/schema.yaml` を作成
- [ ] `shared-types/` に型を生成（`openapi-typescript` を使用）

### ⚙️ CI/CD 構築
- [ ] GitHub Actions を設定
  - [ ] apps/web の format / lint / test
  - [ ] apps/api の format / lint / test

### 🚀 デプロイ戦略
- [ ] apps/web → Vercel にデプロイ
- [ ] apps/api → Railway / Render / Fly.io などにデプロイ
  - [ ] Docker 対応構成の整備

### 🧩 開発環境・拡張パーツ
- [ ] Shade UI を導入（開発スピード向上のため）
- [ ] Prisma or SQLModel の導入（APIの永続化層）
- [ ] ログイン / サインアップ機能（Google OAuth or Email）
- [ ] ユーザーダッシュボードの雛形作成
- [ ] メール送信・通知機能の準備（SendGrid など）

### 🧪 テスト・品質向上
- [ ] フロントエンド：Jest / React Testing Library 導入
- [ ] バックエンド：pytest + HTTPX によるAPIテスト

---

## 💡 アイデアメモ
- コマンド系統を `makefile` にまとめる
- Storybook を導入して UI コンポーネントを整理
- `apps/web` / `apps/api` に `README.md` をそれぞれ作成