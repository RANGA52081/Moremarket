--
-- PostgreSQL database dump
--



-- Dumped from database version 18.2
-- Dumped by pg_dump version 18.2


--
-- Data for Name: adminpanel_adminuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.adminpanel_adminuser (id, username, email, password, is_active, created_at) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	3	add_permission
6	Can change permission	3	change_permission
7	Can delete permission	3	delete_permission
8	Can view permission	3	view_permission
9	Can add group	2	add_group
10	Can change group	2	change_group
11	Can delete group	2	delete_group
12	Can view group	2	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add admin user	7	add_adminuser
26	Can change admin user	7	change_adminuser
27	Can delete admin user	7	delete_adminuser
28	Can view admin user	7	view_adminuser
29	Can add banner	9	add_banner
30	Can change banner	9	change_banner
31	Can delete banner	9	delete_banner
32	Can view banner	9	view_banner
33	Can add banner image	10	add_bannerimage
34	Can change banner image	10	change_bannerimage
35	Can delete banner image	10	delete_bannerimage
36	Can view banner image	10	view_bannerimage
37	Can add user otp	11	add_userotp
38	Can change user otp	11	change_userotp
39	Can delete user otp	11	delete_userotp
40	Can view user otp	11	view_userotp
41	Can add user profile	12	add_userprofile
42	Can change user profile	12	change_userprofile
43	Can delete user profile	12	delete_userprofile
44	Can view user profile	12	view_userprofile
45	Can add address	8	add_address
46	Can change address	8	change_address
47	Can delete address	8	delete_address
48	Can view address	8	view_address
49	Can add product	13	add_product
50	Can change product	13	change_product
51	Can delete product	13	delete_product
52	Can view product	13	view_product
53	Can add product image	14	add_productimage
54	Can change product image	14	change_productimage
55	Can delete product image	14	delete_productimage
56	Can view product image	14	view_productimage
57	Can add product variant	15	add_productvariant
58	Can change product variant	15	change_productvariant
59	Can delete product variant	15	delete_productvariant
60	Can view product variant	15	view_productvariant
61	Can add wishlist	16	add_wishlist
62	Can change wishlist	16	change_wishlist
63	Can delete wishlist	16	delete_wishlist
64	Can view wishlist	16	view_wishlist
65	Can add address	17	add_address
66	Can change address	17	change_address
67	Can delete address	17	delete_address
68	Can view address	17	view_address
69	Can add cart	18	add_cart
70	Can change cart	18	change_cart
71	Can delete cart	18	delete_cart
72	Can view cart	18	view_cart
73	Can add cart item	19	add_cartitem
74	Can change cart item	19	change_cartitem
75	Can delete cart item	19	delete_cartitem
76	Can view cart item	19	view_cartitem
77	Can add order	20	add_order
78	Can change order	20	change_order
79	Can delete order	20	delete_order
80	Can view order	20	view_order
81	Can add order item	21	add_orderitem
82	Can change order item	21	change_orderitem
83	Can delete order item	21	delete_orderitem
84	Can view order item	21	view_orderitem
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
7	pbkdf2_sha256$1200000$nutfoHkvyfTIQhPxmkfvj8$TjHDrya7VW80+sWT0QRdpboWxKroi17pkCMmMzt+qyE=	2026-02-25 09:50:27.119+05:30	f	Ranga52			pranganathan844@gmail.com	f	t	2026-02-25 09:50:00.303+05:30
8	pbkdf2_sha256$1200000$giDD8NtgrJTQvwIKugtzdZ$LEoU4vy1fRYjTexnnnjcw8VsYmvNT5NYE98OkmHFO4E=	2026-02-25 10:00:26.557+05:30	f	karthick			karthick@ydesavvy.com	f	t	2026-02-25 09:59:57.035+05:30
9	pbkdf2_sha256$1200000$k15jxaMPN7ALEZlGwCvaLh$0CD5da1ErQ4YfWOoIRccMMNyfrMe0fFYRMSyxayyQz4=	2026-02-26 12:39:40.456+05:30	f	Thamarai			vs4823533@gmail.com	f	t	2026-02-26 12:39:02.468+05:30
10	pbkdf2_sha256$1200000$JIIbF63c5r1UoIw0XVTJF0$ASgCOl6cVIhMObSAHz4j39Jqle2JELOzUZ+ECCHrCA8=	2026-02-27 09:15:34.818+05:30	f	admin				t	t	2026-02-26 12:54:43.385+05:30
1	pbkdf2_sha256$1200000$zx3B1zFFpCiDnAMo15ioC3$2tcqk5SGG1KqZFddFf4fagld6MdO2/rsFvOUwmmhqO0=	2026-02-28 09:15:52.14517+05:30	t	Ranga52081				t	t	2026-02-23 15:43:15.247+05:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: customer_address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_address (id, full_name, phone, address_line, city, state, pincode, is_default, user_id) FROM stdin;
\.


--
-- Data for Name: customer_banner; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_banner (id, title, subtitle, image, is_active, created_at) FROM stdin;
1	Scaffolding	Scaffolding	banners/Screenshot_2026-02-25_105548_eojBHZO.png	t	2026-02-25 10:58:55.902+05:30
2	VERTICAL	vertical	banners/Gemini_Generated_Image_r5lyh6r5lyh6r5ly.png	t	2026-02-25 11:02:28.683+05:30
\.


--
-- Data for Name: customer_bannerimage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_bannerimage (id, image, "order", banner_id) FROM stdin;
\.


--
-- Data for Name: customer_userotp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_userotp (id, otp, created_at, attempts, user_id) FROM stdin;
\.


--
-- Data for Name: customer_userprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_userprofile (id, phone, profile_image, user_id) FROM stdin;
1		profiles/diffe.png	9
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2026-02-27 15:05:36.866679+05:30	1	Vertical	2	[{"changed": {"name": "product variant", "object": "Vertical - 0.5", "fields": ["Color"]}}]	13	1
2	2026-02-27 15:07:03.868552+05:30	1	Vertical	2	[{"changed": {"name": "product variant", "object": "Vertical - 1.5", "fields": ["Color"]}}]	13	1
3	2026-02-27 15:07:13.817542+05:30	1	Vertical	2	[{"changed": {"name": "product variant", "object": "Vertical - 2", "fields": ["Color"]}}]	13	1
4	2026-02-27 15:07:35.741526+05:30	1	Vertical	2	[{"changed": {"name": "product variant", "object": "Vertical - 1.5", "fields": ["Color"]}}, {"changed": {"name": "product variant", "object": "Vertical - 2", "fields": ["Color"]}}]	13	1
5	2026-02-27 15:11:10.445749+05:30	2	Ledgers	1	[{"added": {}}, {"added": {"name": "product image", "object": "Image of Ledgers"}}, {"added": {"name": "product image", "object": "Image of Ledgers"}}]	13	1
6	2026-02-27 15:12:11.804695+05:30	2	Ledgers	2	[{"changed": {"fields": ["Is featured"]}}]	13	1
7	2026-02-27 15:26:13.506211+05:30	2	Ledgers	2	[{"added": {"name": "product variant", "object": "Ledgers - 2.5"}}]	13	1
8	2026-02-27 15:34:07.72937+05:30	3	Prop Jacks	1	[{"added": {}}, {"added": {"name": "product image", "object": "Image of Prop Jacks"}}, {"added": {"name": "product image", "object": "Image of Prop Jacks"}}, {"added": {"name": "product variant", "object": "Prop Jacks - 2X2"}}, {"added": {"name": "product variant", "object": "Prop Jacks - 2X3"}}]	13	1
9	2026-02-27 16:07:23.591725+05:30	3	Prop Jacks	2	[{"added": {"name": "product variant", "object": "Prop Jacks - 3X3"}}]	13	1
10	2026-02-28 09:17:40.08912+05:30	3	Prop Jacks	2	[]	13	1
11	2026-02-28 09:23:53.247511+05:30	4	Acro Span	1	[{"added": {}}, {"added": {"name": "product variant", "object": "Acro Span - 3m x 3m"}}, {"added": {"name": "product variant", "object": "Acro Span - 2.4m x 2.4m"}}, {"added": {"name": "product variant", "object": "Acro Span - 2m x 2m"}}]	13	1
12	2026-02-28 09:28:42.335056+05:30	4	Acro Span	2	[{"added": {"name": "product image", "object": "Image of Acro Span"}}, {"added": {"name": "product image", "object": "Image of Acro Span"}}, {"added": {"name": "product image", "object": "Image of Acro Span"}}]	13	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	group
3	auth	permission
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	adminpanel	adminuser
8	customer	address
9	customer	banner
10	customer	bannerimage
11	customer	userotp
12	customer	userprofile
13	products	product
14	products	productimage
15	products	productvariant
16	products	wishlist
17	orders	address
18	orders	cart
19	orders	cartitem
20	orders	order
21	orders	orderitem
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2026-02-25 14:54:34.564508+05:30
2	auth	0001_initial	2026-02-25 14:54:34.613411+05:30
3	admin	0001_initial	2026-02-25 14:54:34.628511+05:30
4	admin	0002_logentry_remove_auto_add	2026-02-25 14:54:34.633763+05:30
5	admin	0003_logentry_add_action_flag_choices	2026-02-25 14:54:34.638759+05:30
6	contenttypes	0002_remove_content_type_name	2026-02-25 14:54:34.651004+05:30
7	auth	0002_alter_permission_name_max_length	2026-02-25 14:54:34.656923+05:30
8	auth	0003_alter_user_email_max_length	2026-02-25 14:54:34.664782+05:30
9	auth	0004_alter_user_username_opts	2026-02-25 14:54:34.669774+05:30
10	auth	0005_alter_user_last_login_null	2026-02-25 14:54:34.675994+05:30
11	auth	0006_require_contenttypes_0002	2026-02-25 14:54:34.677114+05:30
12	auth	0007_alter_validators_add_error_messages	2026-02-25 14:54:34.682575+05:30
13	auth	0008_alter_user_username_max_length	2026-02-25 14:54:34.691459+05:30
14	auth	0009_alter_user_last_name_max_length	2026-02-25 14:54:34.697144+05:30
15	auth	0010_alter_group_name_max_length	2026-02-25 14:54:34.703415+05:30
16	auth	0011_update_proxy_permissions	2026-02-25 14:54:34.709083+05:30
17	auth	0012_alter_user_first_name_max_length	2026-02-25 14:54:34.71527+05:30
18	customer	0001_initial	2026-02-25 14:54:34.72118+05:30
19	customer	0002_address	2026-02-25 14:54:34.73577+05:30
20	customer	0003_userotp	2026-02-25 14:54:34.747844+05:30
21	customer	0004_product	2026-02-25 14:54:34.752633+05:30
22	customer	0005_remove_address_user_delete_product_delete_address	2026-02-25 14:54:34.777366+05:30
23	products	0001_initial	2026-02-25 14:54:34.792935+05:30
24	orders	0001_initial	2026-02-25 14:54:34.858796+05:30
25	products	0002_product_is_active_alter_product_category_and_more	2026-02-25 14:54:34.869283+05:30
26	sessions	0001_initial	2026-02-25 14:54:34.877445+05:30
27	adminpanel	0001_initial	2026-02-27 14:21:38.13742+05:30
28	customer	0006_address_userprofile	2026-02-27 14:21:38.177609+05:30
29	products	0003_alter_product_options_alter_productvariant_options_and_more	2026-02-27 14:21:38.213728+05:30
30	products	0004_alter_productvariant_options	2026-02-27 14:21:38.217836+05:30
31	products	0005_rename_price_productvariant_original_price_and_more	2026-02-27 14:21:38.246524+05:30
32	products	0006_productvariant_color	2026-02-27 14:21:38.25162+05:30
33	customer	0007_bannerimage	2026-02-27 14:48:27.702276+05:30
34	orders	0002_alter_cart_user_alter_cartitem_unique_together	2026-02-28 11:09:05.387229+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
oy4d83jeb22nxckiw9d3yubupxu4qgup	.eJxVjDkOwjAQAP-yNbJifGSTkj5vsNbeNQ4gW8pRIf6OIqWAdmY0bwi0byXsqyxhZhhBw-WXRUpPqYfgB9V7U6nVbZmjOhJ12lVNjeV1O9u_QaG1wAjeDWJIrCOXxfmMWuvekk2MOSdB6zseJPnIMVLXsdcGBT32mLWRq4HPF_fTOEQ:1vwBH6:J5lnUPdRpwp3H6yOckxkURXjYZqcQEr6PKxTIOyCg7Q	2026-03-14 09:15:52.146511+05:30
\.


--
-- Data for Name: orders_address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_address (id, full_name, phone, area, city, state, pincode, is_default, created_at, user_id) FROM stdin;
\.


--
-- Data for Name: orders_cart; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_cart (id, created_at, user_id) FROM stdin;
1	2026-02-26 14:27:22.217+05:30	1
\.


--
-- Data for Name: orders_cartitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_cartitem (id, quantity, cart_id, variant_id) FROM stdin;
4	2	1	11
1	1	1	1
3	3	1	7
5	1	1	6
2	4	1	5
\.


--
-- Data for Name: orders_order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_order (id, total_amount, total_weight, status, created_at, address_id, user_id) FROM stdin;
\.


--
-- Data for Name: orders_orderitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_orderitem (id, quantity, price, order_id, variant_id) FROM stdin;
\.


--
-- Data for Name: products_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products_product (id, name, description, category, is_featured, created_at, is_active, slug) FROM stdin;
1	Vertical	Verticals are manufactured from 48.3 mm\r\nO.D. Tube with \r\n3.2mm thickness.	MS	t	2026-02-25 13:33:45.268+05:30	t	hello
2	Ledgers	Cup lock ledgers are used as the main horizontal connecting members. Ledgers are manufactured from 48.3 mm O.D. Tube with 3.2 mm thickness. Standard Sizes are 2.5m, 2m, 1.8m, 1.5m, 1.2m, 0.9m, 0.6m.	MS	t	2026-02-27 15:11:10.441363+05:30	t	ledgers
3	Prop Jacks	They are most economical supports elements to all kind of formwork for slabs, columns, beams and walls. Props are manufactured with outer member 60.3mm O.D. and inner member 48.3 mm O.D. Standard Sizes are 2X2m, 2X3m, 3X3m.Give me Image for This Original image which is used in construction site	MS	t	2026-02-27 15:34:07.722139+05:30	t	prop-jacks
4	Acro Span	Acro span is used as self-supporting runners in shuttering system under the shuttering plates. \r\nAcro span is manufactured with sheets of thickness 2mm and rods of diameter 10mm. \r\nStandard Sizes are 3m x 3m, 2.4m x 2.4m, 2m x 2m.	MS	t	2026-02-28 09:23:53.244697+05:30	t	acro-span
\.


--
-- Data for Name: products_productimage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products_productimage (id, image, product_id) FROM stdin;
1	products/gallery/Screenshot_2026-02-25_133330.png	1
2	products/gallery/ms-standard-vertical-scaffolding.jpg	1
3	products/gallery/product-jpeg-500x500-3.png	1
4	products/gallery/Screenshot_2026-02-27_150955.png	2
5	products/gallery/Screenshot_2026-02-27_151022.png	2
6	products/gallery/Screenshot_2026-02-27_152911.png	3
7	products/gallery/Screenshot_2026-02-27_152931.png	3
8	products/gallery/Screenshot_2026-02-28_091904.png	4
9	products/gallery/Screenshot_2026-02-28_091930.png	4
10	products/gallery/3-spans-on-hire-1-ek5hq.png	4
\.


--
-- Data for Name: products_productvariant; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products_productvariant (id, size, weight, original_price, product_id, is_default, stock, discount_percent, color) FROM stdin;
1	3	14.00	71.00	1	t	10	15	\N
2	2.5	11.05	65.00	1	t	5	10	\N
5	0.5	3.00	75.00	1	t	20	15	blue
4	1.5	5.00	48.00	1	t	10	0	Red
3	2	9.50	55.00	1	t	10	0	Green
6	2.5	8.50	71.00	2	t	8	0	\N
7	2X2	16.50	80.00	3	f	10	0	\N
8	2X3	22.00	85.00	3	f	20	0	\N
9	3X3	18.00	90.00	3	f	10	0	\N
10	3m x 3m	900.00	71.00	4	t	20	0	\N
11	2.4m x 2.4m	41.00	74.00	4	t	10	0	\N
12	2m x 2m	800.00	75.00	4	t	10	0	\N
\.


--
-- Data for Name: products_wishlist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products_wishlist (id, created_at, product_id, user_id) FROM stdin;
\.


--
-- Name: adminpanel_adminuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.adminpanel_adminuser_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 84, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 10, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: customer_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_address_id_seq', 1, false);


--
-- Name: customer_banner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_banner_id_seq', 2, true);


--
-- Name: customer_bannerimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_bannerimage_id_seq', 1, false);


--
-- Name: customer_userotp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_userotp_id_seq', 1, false);


--
-- Name: customer_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_userprofile_id_seq', 1, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 12, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 21, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 34, true);


--
-- Name: orders_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_address_id_seq', 1, false);


--
-- Name: orders_cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_cart_id_seq', 1, true);


--
-- Name: orders_cartitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_cartitem_id_seq', 5, true);


--
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);


--
-- Name: orders_orderitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_orderitem_id_seq', 1, false);


--
-- Name: products_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_product_id_seq', 4, true);


--
-- Name: products_productimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_productimage_id_seq', 10, true);


--
-- Name: products_productvariant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_productvariant_id_seq', 12, true);


--
-- Name: products_wishlist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_wishlist_id_seq', 13, true);


--
-- Name: adminpanel_adminuser adminpanel_adminuser_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

