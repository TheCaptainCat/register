import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "@/views/home/Home.vue";
import adminRoutes from "@/router/admin";

const routes: Array<RouteRecordRaw> = [
  {
    name: "Home",
    path: "/",
    component: Home,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

const addRoutes = (routes: RouteRecordRaw[]): void => {
  for (const route of routes) router.addRoute(route);
};

addRoutes(adminRoutes);

export default router;
