
import { apiFetch } from "./client";
import type { components } from "@shared-types/api-types"; 
type User = components["schemas"]["User"];

export async function getUsers(): Promise<User[]> {
  return apiFetch<User[]>("/users");
}