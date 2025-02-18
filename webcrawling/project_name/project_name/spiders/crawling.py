import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example_saramin'

    def start_requests(self):
        urls = [
            'https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword=it']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        job_count = 0
        print("\n총", len(response.css('div.item_recruit')), "개의 채용공고가 검색되었습니다.")

        for job in response.css('div.item_recruit'):
            job_count += 1

            href = job.css('h2.job_tit a::attr(href)').get()
            if href:
                detail_url = href.replace('&amp;', '&')
                full_url = f'https://www.saramin.co.kr{detail_url}'

                yield scrapy.Request(
                    full_url,
                    callback=self.parse_detail,
                    meta={
                        'job_count': job_count,
                        'company': job.css('strong.corp_name a::text').get('').strip(),
                        'title': job.css('h2.job_tit a span::text').get('').strip(),
                        'conditions': [cond.strip() for cond in job.css('div.job_condition span::text').getall() if cond.strip()],
                        'sectors': [sector.strip() for sector in job.css('div.job_sector a::text').getall() if sector.strip()],
                        'deadline': job.css('div.job_date span.date::text').get('').strip().replace('~', '').strip(),
                        'reg_date': job.css('span.job_day::text').get('').strip().replace('등록일', '').strip()
                    }
                )

        next_page = response.css('a.btnNext::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):
        data = response.meta

        # 우대사항 추출
        preferences = []
        preference_elements = response.css('dd[data-origin*="우대"]::text, dd[data-origin*="우대사항"]::text').getall()
        if preference_elements:
            preferences = [pref.strip() for pref in preference_elements if pref.strip()]

        # 복리후생 추출
        benefits = []
        benefit_elements = response.css('dd[data-origin*="복리후생"]::text, div.jv_benefit dd::text').getall()
        if benefit_elements:
            benefits = [benefit.strip() for benefit in benefit_elements if benefit.strip()]

        print("\n" + "=" * 80)
        print(f"채용공고 #{data['job_count']}")
        print(f"회사명: {data['company']}")
        print(f"제목: {data['title']}")
        print(f"근무조건: {', '.join(data['conditions'])}")
        print(f"직무분야: {', '.join(data['sectors'])}")
        print(f"마감일: {data['deadline']}")
        print(f"등록일: {data['reg_date']}")
        print("+")

        print("우대사항:")
        if preferences:
            for pref in preferences:
                print(f"- {pref}")
        else:
            print("(우대사항 정보 없음)")

        print("\n복리후생:")
        if benefits:
            for benefit in benefits:
                print(f"- {benefit}")
        else:
            print("(복리후생 정보 없음)")

        print("=" * 80)

        data['preferences'] = preferences
        data['benefits'] = benefits
        yield data