import Role from "@/models/role";

export default interface User {
  username: string;
  roles: Role[];
}
