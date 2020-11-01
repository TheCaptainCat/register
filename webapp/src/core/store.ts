import { reactive, readonly } from "vue";

export abstract class Store<T extends object> {
  protected _state: T;

  public constructor() {
    const data = this.data();
    this._state = reactive(data) as T;
  }

  protected abstract data(): T;

  public get state(): T {
    return readonly(this._state) as T;
  }

  public setState(values: Partial<T>) {
    const fields = { ...this._state, ...values } as T;
    for (const key in fields) {
      if (this._state[key] !== fields[key]) this._state[key] = fields[key];
    }
  }
}
