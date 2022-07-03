%% 1. ck2 history titles
% % % all money go my home
% str = {'k_germany', 'd_brandenburg', 'c_havelberg', 'c_brandenburg', 'c_havelberg', 'c_meissen', 'c_gorlitz', 'c_lausitz', 'c_plauen', 'c_mecklemburg', 'c_hamburg', 'c_lubeck', 'c_anhalt', 'd_pommerania', 'c_rostock', 'c_werle', 'c_rugen', 'c_wolgast', 'c_stettin', 'c_neumark', 'c_danzig', 'c_bytow', 'c_slupsk', 'd_bohemia', 'c_domazlice', 'c_praha', 'c_litomerice', 'c_hradec', 'c_plzen', 'c_zatec', 'c_znojmo', 'c_olomouc', 'c_brno', 'c_opava', 'd_holland', 'c_holland', 'c_sticht', 'c_westfriesland', 'c_zeeland', 'c_gelre', 'c_overijssel', 'c_ostfriesland', 'c_frisia', 'd_flanders', 'c_brabant', 'c_hainaut', 'c_breda', 'c_artois', 'c_boulogne', 'c_guines', 'c_yperen', 'c_brugge', 'c_gent', 'd_bavaria', 'c_passau', 'c_oberbayern', 'c_regensburg', 'c_niederbayern', 'c_nurnberg', 'c_eichstadt', 'c_tirol', 'c_innsbruck', 'c_trent', 'c_bolzano', 'd_osterreich', 'c_salzburg', 'c_pongau', 'c_steiermark', 'c_traungau', 'c_krems', 'c_osterreich', 'c_freistadt', 'c_medelike', 'c_leoben', 'c_graz', 'c_pitten', 'd_upper_lorraine', 'c_lorraine', 'c_saintois', 'c_bar', 'c_verdun', 'c_besancon', 'c_amous', 'c_escuens', 'c_montbeliard', 'c_vesoul', 'd_lower_lorraine', 'c_trier', 'c_metz', 'c_saargau', 'c_luxembourg', 'c_liege', 'c_julich', 'c_loon', 'c_koln', 'c_kleve', 'c_berg', 'd_saxony', 'c_altmark', 'c_luneburg', 'c_braunschweig', 'c_verden', 'c_magdeburg', 'c_bremen', 'c_celle', 'c_osnabruck', 'c_oldenburg', 'c_minden', 'c_munster', 'c_gottingen', 'd_hesse', 'c_hesse', 'c_nassau', 'c_frankfurt', 'c_thuringen', 'c_weimar', 'c_leiningen', 'c_wurzburg', 'c_bamberg', 'c_rottenburg', 'c_pfalz', 'c_mainz', 'd_baden', 'c_baden', 'c_breisgau', 'c_zurichgau', 'c_st_gallen', 'c_chur', 'c_schwyz', 'c_schwaben', 'c_ulm', 'c_furstenberg', 'c_wurttemberg', 'c_kempten', 'c_nordgau', 'c_sundgau'};
% fpath = 'C:\Users\peng_\Documents\Paradox Interactive\Crusader Kings II\mod\5_test\history\titles\';
% for k = 1 : numel(str)
% 	fid = fopen([fpath, str{k}, '.txt'], 'w');
% 	fprintf(fid, '936.1.1 = \n{\n\tholder = 999000	\n\tliege = k_germany \n}');
% 	fclose(fid);
% end

%% 2. ck2 history titles + province
% % % 2.1 prepare data
str1 = 'd_upper_burgundy';
str2 = {'c_neuchatel', 'c_bern', 'c_aargau', 'c_vaud', 'c_zurichgau', 'c_st_gallen', 'c_chur', 'c_schwyz'};
str3 = {'b_neuchatel', 'b_stimier', 'b_erguel', 'b_estavayer', 'b_avenches', 'b_colombier', 'b_valangin';
'b_bern', 'b_unterseen', 'b_luzern', 'b_biel', 'b_thun', 'b_murten', 'b_sursee';
'b_basel', 'b_habsburg', 'b_st_ursanne', 'b_porrentruy', 'b_delemont', 'b_moutier', 'b_solothurn';
'b_lausanne', 'b_echallens', 'b_yverdon', 'b_romainmotier', 'b_gruyere', 'b_payerne', 'b_ouchy';
'b_zurich', 'b_winterthur', 'b_swiss_baden', 'b_aarau', 'b_kappel', 'b_kyburg', 'b_toggenburg';
'b_rheineck', 'b_stgallen', 'b_appenzell', 'b_frauenfeld', 'b_altstatten', 'b_lichtensteig', 'b_vaduz';
'b_chur', 'b_churwalden', 'b_davos', 'b_maienfeld', 'b_illanz', 'b_thusis', 'b_glurns';
'b_schwyz', 'b_engelberg', 'b_glarus', 'b_altdorf', 'b_schanis', 'b_disentis', 'b_kussnacht'};
fpath1 = 'C:\Users\peng_\Documents\Paradox Interactive\Crusader Kings II\mod\basel\history\titles\';
fpath2 = 'C:\Users\peng_\Documents\Paradox Interactive\Crusader Kings II\mod\basel\history\provinces\';
str4 = {'ca_wall_q_1', 'ca_wall_q_2', 'ca_wall_q_3', 'ca_wall_q_4', 'ca_wall_q_5', 'ca_wall_1', 'ca_wall_2', 'ca_wall_3', 'ca_wall_4', 'ca_wall_5', 'ca_keep_1', 'ca_keep_2', 'ca_keep_3', 'ca_keep_4', 'ca_keep_5', 'ca_keep_6', 'ca_militia_barracks_1', 'ca_militia_barracks_2', 'ca_militia_barracks_3', 'ca_militia_barracks_4', 'ca_training_grounds_1 ', 'ca_training_grounds_2', 'ca_training_grounds_3 ', 'ca_barracks_1', 'ca_barracks_2', 'ca_barracks_3', 'ca_barracks_4', 'ca_barracks_5', 'ca_barracks_6', 'ca_stable_1', 'ca_stable_2', 'ca_stable_3', 'ca_stable_4', 'ca_stable_5', 'ca_stable_6', 'ca_town_1', 'ca_town_2', 'ca_town_3', 'ca_town_4', 'ca_town_5', 'ca_town_6', 'ca_culture_frank_norman_german_1', 'ca_culture_frank_norman_german_2', 'ca_culture_frank_norman_german_3', 'ca_culture_frank_norman_german_4'};
% % % 2.2 print titles
[N, M] = size(str3);
X = numel(str4);
% % % duchy
fid = fopen([fpath1, str1, '.txt'], 'w');
fprintf(fid, '936.1.1 = \n{\n\tholder = 999000	\n\tliege = k_germany \n}');
fclose(fid);

for k = 1 : N
	% % % county	
	fid = fopen([fpath1, str2{k}, '.txt'], 'w');
	fprintf(fid, ['936.1.1 = \n{\n\tholder = 999000	\n\tliege = ', str1, ' \n}']);
	fclose(fid);
	
	for l = 1 : M
		% % % barony
		fid = fopen([fpath1, str3{k, l}, '.txt'], 'w');
		fprintf(fid, ['936.1.1 = \n{\n\tholder = 999000	\n\tliege = ', str2{k}, ' \n}']);
		fclose(fid);
	end
	
	% % % county	
	fid = fopen([fpath2, str2{k}, '.txt'], 'w');
	fprintf(fid, ['title = ', str2{k}, '\n\nculture = german\nreligion = catholic\n\nmax_settlements = 7\n']);
	for l = 1 : M
		fprintf(fid, [str3{k, l}, ' = castle\n']);
	end
	fprintf(fid, ['900.1.1 = {\n\tcapital = ', str3{k, 1}, '\n\n']);
	for l = 1 : M
		for x = 1 : X
			fprintf(fid, ['\t', str3{k, l},'=', str4{x}, '\n']);
		end
		fprintf(fid, '\n');
	end
	fprintf(fid, '}\n');
	fclose(fid);
end

