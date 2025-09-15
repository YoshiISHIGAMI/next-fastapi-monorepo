# 📦 next-fastapi-monorepo

English follows Japanese. / 日本語のあとに英語が続きます。

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

# 📦 next-fastapi-monorepo

## 📝 Overview (in English)

This repository is a **modern monorepo template** that integrates **Next.js (TypeScript)** and **FastAPI (Python)**.

It uses **OpenAPI** to define API schemas and share types between the frontend and backend via the `shared-types` directory.

## 🛠 Tech Stack

| Area         | Tech Used                                      |
|--------------|------------------------------------------------|
| Frontend     | Next.js, TypeScript, Tailwind CSS              |
| Backend      | FastAPI, Python, Poetry                        |
| API Docs     | Swagger UI / Redoc (via FastAPI)               |
| Type Sharing | OpenAPI → `shared-types` (auto generated)      |
| Monorepo     | Turborepo + pnpm workspace                     |
