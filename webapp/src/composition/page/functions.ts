import ApiRequest from "@/core/api";
import { HttpMethod } from "@/core/requests";
import { reactive } from "vue";
import Page, { PartialPage } from "@/composition/page/models";

export interface PageState {
  page?: Page;
  loading: boolean;
}

export interface PageListState {
  pages: PartialPage[];
  loading: boolean;
}

function newPageState(loading: boolean) {
  return reactive<PageState>({
    page: undefined,
    loading
  });
}

function newPageListState(loading: boolean) {
  return reactive<PageListState>({
    pages: [],
    loading
  });
}

async function getPage(state: PageState, articleId: number, language: string) {
  state.loading = true;
  const request = new ApiRequest(
    HttpMethod.get,
    `/page/${language}/${articleId}`
  );
  const response = await request.fetch<Page>();
  state.page = response.data;
  state.loading = false;
}

async function getPagesByLanguage(state: PageListState, language: string) {
  state.loading = true;
  const request = new ApiRequest(HttpMethod.get, `/page/${language}`);
  const response = await request.fetch<PartialPage[]>();
  state.pages = response.data;
  state.loading = false;
}

async function addVersion(
  state: PageState,
  articleId: number,
  language: string,
  content: string
) {
  const request = new ApiRequest(
    HttpMethod.patch,
    `/page/${language}/${articleId}`,
    {
      content
    }
  );
  const response = await request.fetch<Page>();
  state.page = response.data;
}

async function fetchContent(articleId: number, language: string) {
  const request = new ApiRequest(
    HttpMethod.get,
    `/page/${language}/${articleId}/content`
  );
  await request.fetch();
}

export default function usePage() {
  return {
    newPageState,
    newPageListState,
    getPage,
    getPagesByLanguage,
    addVersion,
    fetchContent
  };
}
