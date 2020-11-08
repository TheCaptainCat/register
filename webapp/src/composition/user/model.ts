import Role from "@/composition/role/role";

export default interface User {
  username: string;
  roles: Role[];
}
