SELECT
	bid.id, bid.crawled_at, bid.crawled_from, bid.session_at, bid.public_agency, bid.description, bid.modality, bid.codes,
	json_agg(
            json_build_object(
                'published_at', event.published_at, 
                'summary', event.summary
			)
        ) AS events 
FROM public.datasets_cityhallbid bid
LEFT JOIN public.datasets_cityhallbidevent event ON (bid.id = event.bid_id)
GROUP by bid.id;
