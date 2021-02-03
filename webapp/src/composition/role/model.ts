export default interface Role {
  name: string;
}

export const AppRoles: Record<string, Role> = {
  root: { name: "root" },
  admin: { name: "admin" },
  creator: { name: "creator" },
};
