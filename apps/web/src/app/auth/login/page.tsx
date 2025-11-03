"use client";

import { useState } from "react";
import { login } from "@/shared/api/auth";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setMessage("ログイン中...");

    try {
      const res = await login({ email, password });
      setMessage(`✅ ログイン成功！Token: ${res.access_token}`);
    } catch (err) {
      setMessage("❌ ログイン失敗：メールまたはパスワードが間違っています。");
    }
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-black text-white">
      <h1 className="text-3xl font-bold mb-6">Login</h1>
      <form onSubmit={handleSubmit} className="flex flex-col w-80 space-y-4">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="p-2 rounded bg-gray-800 border border-gray-600"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="p-2 rounded bg-gray-800 border border-gray-600"
        />
        <button
          type="submit"
          className="bg-blue-600 hover:bg-blue-500 py-2 rounded font-semibold"
        >
          Login
        </button>
      </form>
      {message && <p className="mt-4">{message}</p>}
    </main>
  );
}