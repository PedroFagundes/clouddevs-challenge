select * from products p
where
	(
		p.visibility_settings = 'default'
		or p.visibility_settings = 'catalog_members' and p.catalog_id in
		(
			select c.id	from catalogs c
			inner join clients_catalog cc on c.id = cc.catalog_id
			where cc.client_id = 2
		)
	)
