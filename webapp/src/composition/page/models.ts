import Article from "@/composition/article/models";
import User from "@/composition/user/model";
import Language from "../language/model";

export default interface Page {
  name: string;
  article: Article;
  language: Language
  created_by: User;
  created_on: Date;
  updated_by: User;
  updated_on: Date;
  last_version: Version;
}

export interface PartialPage {
  name: string;
  language: string;
  article: number;
}

export interface Version {
  content: string;
  created_by: User;
  created_on: Date;
  updated_by: User;
  updated_on: Date;
}
