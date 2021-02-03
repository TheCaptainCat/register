import Role, { AppRoles } from "@/composition/role/model";

const checkPermissions = (roles: Role[] | Role, userRoles: Role[]): boolean => {
  const userRoleNames = userRoles.map((r) => r.name);
  if (Array.isArray(roles)) {
    const roleNames = roles.map((r) => r.name);
    if (userRoleNames.includes(AppRoles.root.name)) return true;
    const intersect = userRoleNames.filter((r) => roleNames.includes(r));
    return intersect.length > 0;
  }
  return userRoleNames.includes(roles.name);
};

export { checkPermissions };
