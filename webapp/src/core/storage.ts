class AppStorage {
  public get<T>(key: string): T | undefined {
    const item = localStorage.getItem(key);
    if (item !== null) return JSON.parse(item) as T;
    return undefined;
  }

  public set<T>(key: string, value: T) {
    localStorage.setItem(key, JSON.stringify(value));
  }
}

const storage = new AppStorage();
export default storage;
