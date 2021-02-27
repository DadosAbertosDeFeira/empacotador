SELECT
	dg.id, dg.crawled_at, dg.crawled_from, dg.notes, dg.date, dg.power, dg.year_and_edition, dg.is_legacy,
	json_agg(
            json_build_object(
                'title', event.title,
                'secretariat', event.secretariat,
                'summary', event.summary,
                'published_on', event.published_on
			)
        ) as events
FROM public.datasets_gazette dg
LEFT JOIN public.datasets_gazetteevent event ON (dg.id = event.gazette_id)
GROUP BY dg.id
