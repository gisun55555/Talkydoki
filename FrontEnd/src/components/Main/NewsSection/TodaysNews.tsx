import { NegativeTitle } from "@/styles/common/ui/text";
import TimerCarousel from "@/components/Main/NewsSection/TimerCarousel";
import { useRecommendNews } from "@/api/newsApi";

function TodaysNews() {
  const { data, isLoading } = useRecommendNews();

  if (isLoading) return <></>;
  if (!data || !data[0]) return <></>;

  return (
    <>
      <NegativeTitle>오늘의 뉴스</NegativeTitle>
      <TimerCarousel width={100} height={40} news={data} />
    </>
  );
}

export default TodaysNews;
