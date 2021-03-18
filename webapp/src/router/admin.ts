import { RouteRecordRaw } from "vue-router";
import UserList from "@/views/admin/Users.vue";

const adminRoutes: Array<RouteRecordRaw> = [
  {
    name: "AdminUserList",
    path: "/admin/users",
    component: UserList,
  },
];

export default adminRoutes;
