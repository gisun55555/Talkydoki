// 단어장 관련 인터페이스

export interface VocaInterface {
  id: number;
  japanese: string;
  japaneseRead: string;
  korean: string;
  type: string;
  personalVocabularyId: number;
}

export interface PersonalVocaInterface {
  personalVocabularyId: number;
  japanese: string;
  japaneseRead: string;
  korean: string;
  type: string;
}

export interface WordSearchInterface {
  id?: number;
  japanese: string;
  japaneseRead: string;
  korean?: string;
  type?: string;
  personalVocabularyId?: null | number;
}
