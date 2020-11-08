import { reactive } from "vue";
import ApiRequest from "@/core/api";
import { HttpMethod } from "@/core/requests";
import Language from "@/composition/language/model";

export interface LanguageState {
  languages: Language[];
  loading: boolean;
}

function newLanguageState() {
  return reactive<LanguageState>({
    languages: [],
    loading: false
  });
}

async function getLanguages(state: LanguageState) {
  state.loading = true;
  const request = new ApiRequest(HttpMethod.get, "/lang");
  const response = await request.fetch<Language[]>();
  state.languages = response.data;
  state.loading = false;
}

async function createLanguage(state: LanguageState, name: string) {
  const request = new ApiRequest(HttpMethod.post, "/lang", { name });
  const response = await request.fetch<Language>();
  state.languages.push(response.data);
}

export default function useLanguage() {
  return {
    newLanguageState,
    getLanguages,
    createLanguage
  };
}
