import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", name: "home", component: HomeView },
    { path: "/blogs", name: "blogs", component: () => import("@/views/BlogView.vue") },
    {
      path: "/admin/create",
      name: "adminCreate",
      component: () => import("@/views/CreateBlogView.vue"),
      meta: { requiresAuth: true },
    },
    {
      path: "/blogs/:id",
      name: "blogDetail",
      component: () => import("@/views/BlogDetailView.vue"),
    },
    {
      path: "/admin/blogs/edit/:id",
      name: "blogEdit",
      component: () => import("@/views/EditBlogView.vue"),
      meta: { requiresAuth: true },
    },
    {
      path: "/login",
      name: "login",
      component: () => import("@/views/LoginView.vue"),
    },
    {
      path: "/register",
      name: "register",
      component: () => import("@/views/RegisterView.vue"),
    },
  ],
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem("access_token");

  if (to.meta.requiresAuth && !isAuthenticated) {
    return next({ name: "login" });
  }

  if ((to.name === "login" || to.name === "register") && isAuthenticated) {
    return next({ name: "home" });
  }

  next();
});

export default router;
