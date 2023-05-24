--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-05-17 19:12:52

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16546)
-- Name: kafedra; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kafedra (
    id integer NOT NULL,
    name character varying NOT NULL,
    dek character varying NOT NULL
);


ALTER TABLE public.kafedra OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16545)
-- Name: kafedra_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kafedra_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kafedra_id_seq OWNER TO postgres;

--
-- TOC entry 3353 (class 0 OID 0)
-- Dependencies: 214
-- Name: kafedra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kafedra_id_seq OWNED BY public.kafedra.id;


--
-- TOC entry 219 (class 1259 OID 16573)
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    id integer NOT NULL,
    name character varying NOT NULL,
    data_pas character varying NOT NULL,
    group_name character varying
);


ALTER TABLE public.student OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16557)
-- Name: student_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_group (
    id integer NOT NULL,
    name character varying NOT NULL,
    kaf character varying
);


ALTER TABLE public.student_group OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16556)
-- Name: student_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_group_id_seq OWNER TO postgres;

--
-- TOC entry 3354 (class 0 OID 0)
-- Dependencies: 216
-- Name: student_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_group_id_seq OWNED BY public.student_group.id;


--
-- TOC entry 218 (class 1259 OID 16572)
-- Name: student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_id_seq OWNER TO postgres;

--
-- TOC entry 3355 (class 0 OID 0)
-- Dependencies: 218
-- Name: student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_id_seq OWNED BY public.student.id;


--
-- TOC entry 3183 (class 2604 OID 16549)
-- Name: kafedra id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kafedra ALTER COLUMN id SET DEFAULT nextval('public.kafedra_id_seq'::regclass);


--
-- TOC entry 3185 (class 2604 OID 16576)
-- Name: student id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student ALTER COLUMN id SET DEFAULT nextval('public.student_id_seq'::regclass);


--
-- TOC entry 3184 (class 2604 OID 16560)
-- Name: student_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group ALTER COLUMN id SET DEFAULT nextval('public.student_group_id_seq'::regclass);


--
-- TOC entry 3343 (class 0 OID 16546)
-- Dependencies: 215
-- Data for Name: kafedra; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.kafedra (id, name, dek) VALUES (1, 'ИТ', 'ИТ');
INSERT INTO public.kafedra (id, name, dek) VALUES (2, 'КИБ', 'ИТ');


--
-- TOC entry 3347 (class 0 OID 16573)
-- Dependencies: 219
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.student (id, name, data_pas, group_name) VALUES (1, 'Федоров Андрей Юрьевич', '8103 492845', 'БВТ2202');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (2, 'Ланцев Петр Иванович', '8118 394758', 'БВТ2202');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (3, 'Волков Сергей Сергеевич', '8114 834353', 'БВТ2202');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (4, 'Никифоров Кирилл Данилович', '8108 293758', 'БВТ2202');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (5, 'Дремко Павел Станиславович', '8114 831047', 'БВТ2202');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (6, 'Угодин Вечяслав Викторович', '8118 092758', 'БВТ2104');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (7, 'Чижиков Алексей Михайлович', '8103 945725', 'БВТ2104');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (8, 'Романова Софья Михайловна', '8108 230486', 'БВТ2104');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (9, 'Орлов Петр Григорьевич', '8108 293424', 'БВТ2104');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (10, 'Морозов Дмитрий Сергеевич', '8114 892645', 'БВТ2104');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (11, 'Потемкин Данил Владимирович', '8118 387358', 'БИБ2007');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (12, 'Пугачев Емельян Иванович', '8118 394714', 'БИБ2007');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (13, 'Болотников Иван Иссаевич', '8103 490185', 'БИБ2007');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (14, 'Мнишик Мария Юрьевна', '8108 299658', 'БИБ2007');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (15, 'Гогин Владислав Кантович', '8114 385453', 'БИБ2007');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (16, 'Руссо Жан Жаккович', '8118 390173', 'БИБ2103');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (17, 'Погодина Ирина Дмитриевна', '8118 374658', 'БИБ2103');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (18, 'Катаев Валентин Дмитриевич', '8103 098725', 'БИБ2103');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (19, 'Иванов Максим Жаргалович', '8118 390298', 'БИБ2103');
INSERT INTO public.student (id, name, data_pas, group_name) VALUES (20, 'Коробков Семен Владимирович', '8114 309475', 'БИБ2103');


--
-- TOC entry 3345 (class 0 OID 16557)
-- Dependencies: 217
-- Data for Name: student_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.student_group (id, name, kaf) VALUES (1, 'БВТ2202', 'ИТ');
INSERT INTO public.student_group (id, name, kaf) VALUES (2, 'БВТ2104', 'ИТ');
INSERT INTO public.student_group (id, name, kaf) VALUES (3, 'БИБ2007', 'КИБ');
INSERT INTO public.student_group (id, name, kaf) VALUES (4, 'БИБ2103', 'КИБ');


--
-- TOC entry 3356 (class 0 OID 0)
-- Dependencies: 214
-- Name: kafedra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kafedra_id_seq', 2, true);


--
-- TOC entry 3357 (class 0 OID 0)
-- Dependencies: 216
-- Name: student_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_group_id_seq', 4, true);


--
-- TOC entry 3358 (class 0 OID 0)
-- Dependencies: 218
-- Name: student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_id_seq', 20, true);


--
-- TOC entry 3187 (class 2606 OID 16555)
-- Name: kafedra kafedra_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kafedra
    ADD CONSTRAINT kafedra_name_key UNIQUE (name);


--
-- TOC entry 3189 (class 2606 OID 16553)
-- Name: kafedra kafedra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kafedra
    ADD CONSTRAINT kafedra_pkey PRIMARY KEY (id);


--
-- TOC entry 3195 (class 2606 OID 16582)
-- Name: student student_data_pas_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_data_pas_key UNIQUE (data_pas);


--
-- TOC entry 3191 (class 2606 OID 16566)
-- Name: student_group student_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT student_group_name_key UNIQUE (name);


--
-- TOC entry 3193 (class 2606 OID 16564)
-- Name: student_group student_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT student_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3197 (class 2606 OID 16580)
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);


--
-- TOC entry 3198 (class 2606 OID 16567)
-- Name: student_group student_group_kaf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT student_group_kaf_fkey FOREIGN KEY (kaf) REFERENCES public.kafedra(name);


--
-- TOC entry 3199 (class 2606 OID 16583)
-- Name: student student_group_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_group_name_fkey FOREIGN KEY (group_name) REFERENCES public.student_group(name);


-- Completed on 2023-05-17 19:12:52

--
-- PostgreSQL database dump complete
--

