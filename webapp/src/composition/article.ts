import request from "@/core/api";
import { reactive } from "vue";
import { User } from "@/composition/user";

// MODEL

interface Historized {
  created_on: string;
  created_by: User;
  updated_on: string;
  updated_by: User;
}

interface Version extends Historized {
  content: string;
}

interface Article extends Historized {
  name: string;
  article: { key: string; languages: Record<string, string> };
  last_version: Version | null;
}

interface PartialArticle {
  name: string;
  language: string;
  article: string;
}

// ARTICLE METHODS

const create = async (
  lang: string,
  name: string,
  linkTo?: string
): Promise<Article> => {
  const path = linkTo ? `/page/${lang}/${linkTo}` : `/page/${lang}`;
  const res = await request.post<{ name: string }, Article>(path, {
    name,
  });
  return res.data;
};

const get = async (lang: string, article: string): Promise<Article> => {
  const res = await request.get<Article>(`/page/${lang}/${article}`);
  return res.data;
};

const update = async (
  lang: string,
  article: Article,
  content: string
): Promise<Article> => {
  const res = await request.patch<{ content: string }, Article>(
    `/page/${lang}/${article.article.key}`,
    { content }
  );
  return res.data;
};

const getContent = async (lang: string, article: Article): Promise<string> => {
  const res = await request.get<string>(
    `/page/${lang}/${article.article.key}/content`
  );
  return res.data;
};

const formatName = (article: string): string => {
  return article
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9 -.]/g, "")
    .replace(/ /g, "_");
};

// USE ARTICLE

interface UseArticleParams {
  create: typeof create;
  get: typeof get;
  update: typeof update;
  getContent: typeof getContent;
  formatName: typeof formatName;
}

const useArticle = (): UseArticleParams => {
  return {
    create,
    get,
    update,
    getContent,
    formatName,
  };
};

// ARTICLES METHODS

const getFromLang = async (lang: string): Promise<PartialArticle[]> => {
  const res = await request.get<PartialArticle[]>(`/page/${lang}`);
  return res.data;
};

const getAvailableLanguages = async (
  article: string
): Promise<Record<string, string>> => {
  const res = await request.get<Record<string, string>>(
    `/article/a/${article}/languages`
  );
  return res.data;
};

// USE ARTICLES

interface ArticlesState {
  articles: PartialArticle[];
  loading: boolean;
}

interface UseArticlesParams {
  state: ArticlesState;
  getFromLang: typeof getFromLang;
  getAvailableLanguages: typeof getAvailableLanguages;
}

const useArticles = (): UseArticlesParams => {
  return {
    state: reactive({ articles: [], loading: false }),
    getFromLang,
    getAvailableLanguages,
  };
};

export { Article, PartialArticle, useArticle, useArticles };
