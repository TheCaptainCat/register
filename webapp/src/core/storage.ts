export default abstract class AppStorage<T extends object> {
  private readonly _key: string;

  protected constructor(key: string) {
    this._key = key;
  }

  public get(): T | null {
    const item = localStorage.getItem(this._key);
    if (item !== null) return JSON.parse(item) as T;
    return null;
  }

  public set(value: T): void {
    localStorage.setItem(this._key, JSON.stringify(value));
  }
}
