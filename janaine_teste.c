/************* SQL  Teste *************/
1- id_customer, cd_address_type;

2-INSERT INTO `tb_customer` (`id_customer`, `nm_customer`, `cpf_cnpj`) VALUES (NULL, 'Joãozinho', '88877766655');
INSERT INTO `tb_customer_address` (`id_customer`, `cd_address_type`, `street`, `lot`, `reference`, `zip_code`)
VALUES ((SELECT `id_customer` FROM `tb_customer` WHERE `cpf_cnpj` = '88877766655'), 'R', 'Rua das Flores', '1', '', '01234567'),
((SELECT `id_customer` FROM `tb_customer` WHERE `cpf_cnpj` = '88877766655'), 'C', 'Rua das Pedras', '100', 'Conjunto 200', '01234567');

3- N endereços podem ser cadastrados para um cliente;

4- DELETE `tb_customer_address`, `tb_customer` FROM `tb_customer_address` INNER JOIN `tb_customer` ON `tb_customer_address`.`id_customer` =
`tb_customer`.`id_customer` WHERE `tb_customer`.`cpf_cnpj`= cpf_ou_cnpj_do_cliente;
