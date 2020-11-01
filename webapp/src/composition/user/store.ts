import { Store } from "@/core/store";
import User from "@/composition/user/model";

interface UserState {
  user?: User;
  loading: boolean;
}

class UserStore extends Store<UserState> {
  public data(): UserState {
    return {
      user: undefined,
      loading: false
    };
  }
}

const userStore: UserStore = new UserStore();
export default userStore;
