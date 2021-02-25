import { App } from "vue";
import fr from "@/i18n/fr";
import en from "@/i18n/en";
import { languageStorage, languageStore } from "@/composition/language";

type LangDefinition = Record<string, string | object>;
type LangStrings = Record<string, string>;

const languages: Record<string, LangDefinition> = {
  fr,
  en,
};

const parseStrings = (prefix: string, node: LangDefinition): LangStrings => {
  const strings: LangStrings = {};
  for (const key in node) {
    const value = node[key];
    if (typeof value === "string") {
      strings[prefix + key] = value;
    } else {
      const substrings = parseStrings(
        prefix + key + ".",
        value as LangDefinition
      );
      for (const subKey in substrings) {
        strings[subKey] = substrings[subKey];
      }
    }
  }
  return strings;
};

const buildI18nStrings = (): Record<string, LangStrings> => {
  const built: Record<string, LangStrings> = {};
  for (const lang in languages) {
    built[lang] = parseStrings("", languages[lang]);
  }
  return built;
};

const i18n = {
  install: (app: App<Element>, options: { default: string }): void => {
    const allStrings = buildI18nStrings();

    let lang = options.default;
    const storedLang = languageStorage.get();
    if (storedLang !== null) {
      lang = storedLang.language;
    }

    languageStore.setLanguage(lang);

    app.config.globalProperties.$t = (key: string) => {
      const lang = languageStore.state.language || options.default;
      if (key in allStrings[lang]) {
        return allStrings[lang][key];
      } else if (key in allStrings[options.default]) {
        return allStrings[options.default][key];
      }
      return key;
    };
  },
};

export default i18n;
