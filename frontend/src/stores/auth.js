import { ref } from "vue";
import { defineStore } from "pinia";
const API_URL = import.meta.env.VITE_API_URL;

export const useAuthStore = defineStore("auth", () => {
  const token = ref(localStorage.getItem("access_token") || null);
  const currentUser = ref(
    localStorage.getItem("userData") ? JSON.parse(localStorage.getItem("userData")) : null
  );

  function setToken(newToken) {
    token.value = newToken;
    localStorage.setItem("access_token", newToken);
  }

  function setUserData(userData) {
    currentUser.value = userData;
    localStorage.setItem("userData", JSON.stringify(userData));
  }

  function logout() {
    token.value = null;
    currentUser.value = null;
    localStorage.removeItem("access_token");
    localStorage.removeItem("userData");
  }

  async function fetchCurrentUser() {
    if (!token.value) return null;
    try {
      const res = await fetch(`${API_URL}/auth/me`, {
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });

      if (!res.ok) throw new Error("Failed to fetch user");

      const data = await res.json();
      setUserData(data);
      return data;
    } catch (err) {
      console.error(err.message);
      logout();
      return null;
    }
  }

  return { token, currentUser, setToken, setUserData, fetchCurrentUser, logout };
});
