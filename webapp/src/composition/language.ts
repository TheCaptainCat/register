import { Store } from "@/core/store";
import AppStorage from "@/core/storage";

interface LanguageStoreState {
  language: string | null;
}

interface LanguageStorageState {
  language: string;
}

class LanguageStorage extends AppStorage<LanguageStorageState> {
  public constructor() {
    super("language");
  }
}

const languageStorage = new LanguageStorage();

class LanguageStore extends Store<LanguageStoreState> {
  protected data(): LanguageStoreState {
    return {
      language: null,
    };
  }

  public setLanguage(language: string) {
    this.setState({ language });
    languageStorage.set({ language });
  }
}

const languageStore = new LanguageStore();

export { languageStore, languageStorage };
