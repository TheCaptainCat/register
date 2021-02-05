import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

const addRoutes = (routes: RouteRecordRaw[]): void => {
  for (const route of routes) router.addRoute(route);
};

export { addRoutes };
export default router;
