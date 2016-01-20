-- ----------------------------
-- Sequence structure for mail_id
-- ----------------------------
CREATE SEQUENCE "public"."mail_id"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 31
 CACHE 1;
SELECT setval('"public"."mail_id"', 1, true);

-- ----------------------------
-- Table structure for mail
-- ----------------------------
DROP TABLE IF EXISTS "public"."mail";
CREATE TABLE "public"."mail" (
"id" int2 DEFAULT nextval('mail_id'::regclass) NOT NULL,
"theme" varchar COLLATE "default",
"to" varchar(255) COLLATE "default",
"from" varchar(255) COLLATE "default",
"message" text COLLATE "default"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Records of mail
-- ----------------------------
INSERT INTO "public"."mail" VALUES ('31', 'test1', 'one@qwe.ru', 'qwe@qwe.ru', 'test');
INSERT INTO "public"."mail" VALUES ('37', 'test2', 'ten@qwe.ru', 'wer@qwe.ru', 'Test message!');

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table mail
-- ----------------------------
ALTER TABLE "public"."mail" ADD PRIMARY KEY ("id");
