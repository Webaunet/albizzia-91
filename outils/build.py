import re,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx=open(R+'/index.html',encoding='utf8').read()
HEADER=re.search(r'<header class="site-header">.*?</header>',idx,re.S).group(0)
FOOTER=re.search(r'<footer class="site-footer">.*?</footer>',idx,re.S).group(0)
PH='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
ML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m3 8 9 6 9-6"/></svg>'
PIN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.800 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
def page(fn,cur,title,desc,body,extra=''):
    h=HEADER.replace(' aria-current="page"','')
    h=h.replace('href="%s"'%cur,'href="%s" aria-current="page"'%cur)
    out=f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=Nunito+Sans:wght@400;700;800&display=swap">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{h}
<main>
{body}
</main>
{FOOTER}
<script src="js/main.js"></script>{extra}
</body>
</html>
'''
    open(R+'/'+fn,'w',encoding='utf8').write(out)

# ---------- Savoir-faire ----------
sf=f'''<section class="sec pagehead bg-cream">
  <div class="wrap">
    <div>
      <span class="eyebrow">Notre savoir-faire</span>
      <h1 style="margin-top:1rem">Quatre métiers, <em>un seul interlocuteur</em></h1>
      <p class="lead">Création, entretien, élagage et décoration de terrasses et balcons : Albizzia vous accompagne de la conception à la réalisation, partout en Île-de-France sud.</p>
      <div class="cta-row"><a class="btn btn-primary" href="contact.html">Demander un devis</a><a class="btn btn-ghost" href="tel:+33624363376">{PH}Appeler le 06 24 36 33 76</a></div>
    </div>
    <div class="mosaic">
      <img src="images/creation-jardin.jpg" width="900" height="491" alt="Massifs, pelouse et allée en gravier aménagés devant une maison contemporaine">
      <img src="images/etetage.jpg" width="1400" height="764" alt="Grand arbre étêté, un élagueur encordé dans les branches">
      <img src="images/terrasse-bois.jpg" width="1400" height="764" alt="Pose d'une terrasse en bois devant une maison en pierre">
    </div>
  </div>
</section>

<section class="sec bg-sage" id="creation">
  <div class="wrap split">
    <div class="ph arch-r"><img src="images/allee-dallee.jpg" width="900" height="491" loading="lazy" alt="Chantier d'une allée dallée dans un jardin"></div>
    <div>
      <span class="eyebrow">01 · Création</span>
      <h2>Création et aménagement paysager</h2>
      <p>Plans de création ou d'embellissement de jardins, de bassins, aménagement de niveaux, d'allées, implantation de haies, pose de clôtures, choix des matériaux et des essences. Albizzia vous conseille de la conception à la réalisation, après une étude personnalisée de votre projet, puis vous propose un devis qui allie vos envies et votre budget.</p>
      <ul class="ticks"><li>Haies décoratives ou brise-vent</li><li>Massifs arborés, floraux, vivaces</li><li>Rocailles</li><li>Gazons traditionnels ou en rouleaux</li><li>Arrosage enterré</li><li>Bassins</li><li>Escaliers de jardin</li><li>Retenues de terre</li><li>Pose de clôtures</li></ul>
    </div>
  </div>
</section>

<section class="sec bg-forest" id="entretien">
  <div class="wrap split rev">
    <div class="ph arch-l"><img src="images/tonte.jpg" width="900" height="502" loading="lazy" alt="Jardinier tondant une pelouse le long d'une haie, devant une maison"></div>
    <div>
      <span class="eyebrow" style="color:var(--blush)">02 · Entretien</span>
      <h2>Entretien des jardins et espaces verts</h2>
      <p>Contrats annuels ou passages ponctuels, pour les particuliers, les entreprises, les collectivités et les résidences, partout en Île-de-France sud.</p>
      <ul class="ticks"><li>Tonte</li><li>Débroussaillage</li><li>Ramassage des feuilles</li><li>Coupe d'entretien des haies</li></ul>
      <p class="note">Agréée « service à la personne » : 50 % de vos dépenses déductibles de vos impôts.</p>
    </div>
  </div>
</section>

<section class="sec bg-cream" id="elagage">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">03 · Gros travaux</span><h2>Élagage et dessouchage</h2><p>Pour accompagner le cycle de vie des jardins et des espaces verts, Albizzia s'équipe d'un matériel de qualité pour les gros travaux.</p></div>
    <div class="grid-3" style="margin-top:0">
      <article class="card"><div class="ph"><img src="images/elagage-chene.jpg" width="1376" height="768" loading="lazy" alt="Élagueur casqué encordé dans un grand chêne, au-dessus d'un jardin"></div><div class="body"><h3>Élagage</h3><p>Taille et réduction des arbres, par des professionnels équipés.</p></div></article>
      <article class="card"><div class="ph"><img src="images/dessouchage.jpg" width="900" height="491" loading="lazy" alt="Souche d'arbre et rogneuse de souche dans un jardin"></div><div class="body"><h3>Dessouchage</h3><p>La souche est retirée à la machine, pour retrouver un terrain utilisable.</p></div></article>
      <article class="card plain"><div class="body"><h3>Broyage</h3><p>Le broyage complète l'élagage et le dessouchage pour traiter les végétaux sur place. Demandez-nous ce qui convient à votre chantier.</p></div></article>
    </div>
  </div>
</section>

<section class="sec bg-blush" id="terrasses">
  <div class="wrap split">
    <div class="ph arch-r"><img src="images/terrasse-bois.jpg" width="1400" height="764" loading="lazy" alt="Pose d'une terrasse en bois devant une maison en pierre"></div>
    <div>
      <span class="eyebrow">04 · Décoration</span>
      <h2 style="color:var(--deep)">Terrasses, balcons et intérieurs</h2>
      <p style="color:#4a2a31">Large choix de fleurs, de plantes vertes dépolluantes et de pots. Les jardiniers paysagistes et horticulteurs vous aident à choisir les essences adaptées à votre environnement, à vos envies et à votre budget. Si vous le souhaitez, ils se chargent de tout : achat, transport, rempotage, tuteurage, installation.</p>
      <ul class="ticks"><li>Balcons fleuris</li><li>Jardinières</li><li>Rempotage</li><li>Tuteurage</li></ul>
    </div>
  </div>
</section>

<section class="sec mini bg-deep">
  <div class="wrap band">
    <div><span class="eyebrow" style="color:var(--blush)">Votre projet</span><h2>Décrivez-nous votre jardin</h2><p>Nous étudions votre projet et vous proposons un devis adapté.</p></div>
    <div class="cta-row"><a class="phone" href="tel:+33624363376">06 24 36 33 76</a><a class="btn btn-light" href="contact.html">Demander un devis</a></div>
  </div>
</section>'''
page('savoir-faire.html','savoir-faire.html','Savoir-faire | Albizzia, paysagiste à Angerville (91)','Création de jardins, entretien, élagage, dessouchage, terrasses et balcons : le savoir-faire d\'Albizzia, paysagiste à Angerville.',sf)

# ---------- Qui sommes-nous ----------
qs=f'''<section class="sec pagehead bg-sage">
  <div class="wrap">
    <div>
      <span class="eyebrow">Qui sommes-nous</span>
      <h1 style="margin-top:1rem">Des jardiniers qui ont <em>repris leur entreprise</em></h1>
      <p class="lead">Dany et Ronan Nedelec ont repris Albizzia en octobre 2020, après plus de quinze ans passés comme salariés de la société.</p>
      <div class="cta-row"><a class="btn btn-primary" href="contact.html">Nous rencontrer</a><a class="btn btn-ghost" href="savoir-faire.html">Voir nos métiers</a></div>
    </div>
    <div class="split" style="display:block"><div class="ph arch-r"><img src="images/conception.jpg" width="1400" height="764" style="width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:999px 999px 24px 24px;box-shadow:var(--shadow)" alt="Présentation d'un plan de jardin sur tablette, à côté d'un muret et d'une terrasse"></div></div>
  </div>
</section>

<section class="sec bg-cream">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Notre histoire</span>
      <h2>Trois étapes, une même passion du jardin</h2>
      <ul class="timeline">
        <li><b>1996</b><p>Albizzia est créée par Nathalie Ponthieux, jardinier paysagiste diplômée.</p></li>
        <li><b>Plus de 15 ans de métier</b><p>Dany et Ronan Nedelec travaillent dans l'entreprise comme salariés.</p></li>
        <li><b>Octobre 2020</b><p>Ils reprennent la société et proposent une large palette de services partout en Île-de-France.</p></li>
      </ul>
    </div>
    <div class="ph arch-l"><img src="images/maconnerie.jpg" width="900" height="491" loading="lazy" alt="Paysagiste montant un muret de pierre et des marches dans un jardin"></div>
  </div>
</section>

<section class="sec bg-forest">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow" style="color:var(--blush)">Ce que vous garantit Albizzia</span><h2>Sérieux, savoir-faire et disponibilité</h2><p>Plus de 20 ans d'expérience, une équipe pluridisciplinaire et un matériel de qualité.</p></div>
    <div class="steps c3">
      <div class="step s2"><h3>Une équipe diplômée</h3><p>Des professionnels issus d'écoles horticoles, jardiniers paysagistes et horticulteurs.</p></div>
      <div class="step s1"><h3>Un seul interlocuteur</h3><p>Une personne qualifiée vous suit dès le premier rendez-vous et jusqu'à la finalisation des travaux.</p></div>
      <div class="step s3"><h3>Un matériel adapté</h3><p>De quoi mener les gros travaux comme l'élagage et le dessouchage.</p></div>
    </div>
  </div>
</section>

<section class="sec mini bg-blush">
  <div class="wrap band" style="grid-template-columns:1.3fr 1fr">
    <div><h2 style="color:var(--deep)">Faites pousser vos envies</h2><p style="color:#4a2a31">Parlons de votre projet autour d'un premier rendez-vous.</p></div>
    <div class="cta-row"><a class="btn btn-primary" href="contact.html">Prendre contact</a><a class="btn btn-ghost" href="tel:+33624363376">{PH}06 24 36 33 76</a></div>
  </div>
</section>'''
page('qui-sommes-nous.html','qui-sommes-nous.html','Qui sommes-nous | Albizzia, paysagiste à Angerville (91)','Histoire et équipe d\'Albizzia : fondée en 1996, reprise en 2020 par Dany et Ronan Nedelec, paysagistes à Angerville.',qs)

# ---------- Économie d'impôts ----------
ei=f'''<section class="sec pagehead bg-blush">
  <div class="wrap">
    <div>
      <span class="eyebrow">Économie d'impôts</span>
      <h1 style="margin-top:1rem;color:var(--deep)">Déduisez <em>50 %</em> de vos dépenses de jardinage</h1>
      <p class="lead" style="color:#4a2a31">Albizzia est agréée « service à la personne ». Les particuliers bénéficient d'une réduction d'impôts de 50 % des sommes versées pour les services de jardinage.</p>
      <div class="cta-row"><a class="btn btn-primary" href="contact.html">Demander un devis</a></div>
    </div>
    <div style="display:grid;place-items:center"><div class="big" style="width:300px;height:300px"><div><b style="font-size:5.4rem">50 %</b><br><span>de réduction d'impôts</span></div></div></div>
  </div>
</section>

<section class="sec bg-cream">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Les travaux concernés</span><h2>L'entretien de votre jardin, au quotidien</h2><p>Le service de jardinage rendu à votre domicile entre dans les services à la personne.</p></div>
    <div class="facts">
      <div class="fact"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 36h36M10 36c0-8 6-14 14-14s14 6 14 14M24 22V10"/></svg><h3>Tonte</h3><p>Entretien régulier de votre pelouse.</p></div>
      <div class="fact"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M24 42V20M24 30c-8 0-12-4-12-12 8 0 12 4 12 12zM24 24c0-8 4-12 12-12 0 8-4 12-12 12z"/></svg><h3>Haies et feuilles</h3><p>Coupe d'entretien des haies, ramassage des feuilles.</p></div>
      <div class="fact"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 40 40 8M14 14l6 6M28 28l6 6"/></svg><h3>Débroussaillage</h3><p>Remise en ordre des espaces enherbés.</p></div>
    </div>
  </div>
</section>

<section class="sec bg-forest">
  <div class="wrap split">
    <div>
      <span class="eyebrow" style="color:var(--blush)">Bon à savoir</span>
      <h2>Plafonds et conditions : vérifiez votre situation</h2>
      <p>Le montant de la réduction dépend de votre foyer fiscal et des plafonds en vigueur. Notre site actuel mentionne plusieurs plafonds selon les pages : confirmez le montant exact auprès de l'administration fiscale ou d'Albizzia avant de vous engager.</p>
      <p class="note">Contrats annuels ou passages ponctuels : le service est le même.</p>
    </div>
    <div class="ph arch-l"><img src="images/entretien.jpg" width="900" height="491" loading="lazy" alt="Jardin entretenu avec pelouse, massifs et allée gravillonnée devant une maison"></div>
  </div>
</section>

<section class="sec mini bg-deep">
  <div class="wrap band">
    <div><h2>Un contrat d'entretien pour votre jardin ?</h2><p>Dites-nous ce dont vous avez besoin : nous vous répondons dans les meilleurs délais.</p></div>
    <div class="cta-row"><a class="phone" href="tel:+33624363376">06 24 36 33 76</a><a class="btn btn-light" href="contact.html">Écrire à Albizzia</a></div>
  </div>
</section>'''
page('economie-impots.html','economie-impots.html','Économie d\'impôts | Albizzia, paysagiste à Angerville (91)','Services à la personne : Albizzia, agréée, permet aux particuliers de déduire 50 % de leurs dépenses de jardinage.',ei)

# ---------- Contact ----------
ct=f'''<section class="sec bg-cream" style="min-height:0;padding-block:64px 120px">
  <div class="wrap contact-grid">
    <div>
      <span class="eyebrow">Contact</span>
      <h1 style="margin-top:1rem;color:var(--forest)">Parlons de votre <em style="color:var(--rose)">jardin</em></h1>
      <p style="color:var(--muted);font-size:1.15rem;margin-top:1.2rem">Remplissez le formulaire : vous obtenez un récapitulatif à nous envoyer par SMS ou par e-mail, ou appelez-nous directement.</p>
      <div class="coords">
        <a class="coord" href="tel:+33624363376">{PH}<span><small>Mobile</small><strong>06 24 36 33 76</strong></span></a>
        <a class="coord" href="tel:+33164540634">{PH}<span><small>Fixe</small><strong>01 64 54 06 34</strong></span></a>
        <a class="coord" href="mailto:contact@albizzia-paysage.com">{ML}<span><small>E-mail</small><strong>contact@albizzia-paysage.com</strong></span></a>
        <div class="coord">{PIN}<span><small>Basés à Angerville (91)</small><strong>Île-de-France sud</strong></span></div>
      </div>
    </div>
    <div class="formcard">
      <h2>Votre demande de devis</h2>
      <form id="devis" novalidate>
        <div class="field"><label for="nom">Nom</label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="nom-err"><div class="err" id="nom-err" role="alert"></div></div>
        <div class="field"><label for="tel">Téléphone</label><input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="tel-err"><div class="err" id="tel-err" role="alert"></div></div>
        <div class="field"><label for="commune">Commune</label><input id="commune" name="commune" type="text" autocomplete="address-level2" required aria-describedby="commune-err"><div class="err" id="commune-err" role="alert"></div></div>
        <div class="field"><label for="besoin">Type de travaux</label><select id="besoin" name="besoin" required aria-describedby="besoin-err"><option value="">Choisir…</option><option>Création et aménagement paysager</option><option>Entretien de jardin et d'espaces verts</option><option>Élagage ou abattage</option><option>Dessouchage ou broyage</option><option>Terrasse, balcon ou intérieur</option><option>Autre demande</option></select><div class="err" id="besoin-err" role="alert"></div></div>
        <div class="field"><label for="message">Message <i>(facultatif)</i></label><textarea id="message" name="message" rows="4"></textarea></div>
        <button class="btn btn-primary" type="submit">Préparer ma demande</button>
      </form>
      <div class="recap" id="recap" aria-live="polite">
        <div class="status">Votre récapitulatif est prêt : choisissez comment l'envoyer.</div>
        <pre id="recap-text"></pre>
        <div class="acts">
          <a class="btn btn-primary" id="sms" href="sms:+33624363376">Envoyer par SMS</a>
          <button class="btn btn-ghost" id="copy" type="button">Copier</button>
          <a class="btn btn-ghost" href="tel:+33624363376">{PH}Appeler</a>
          <a class="btn btn-ghost" id="mail" href="mailto:contact@albizzia-paysage.com">{ML}E-mail</a>
        </div>
        <p id="copy-status" role="status" style="margin-top:.8rem;font-weight:700"></p>
      </div>
    </div>
  </div>
</section>

<section class="sec bg-forest">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow" style="color:var(--blush)">Après votre demande</span><h2>Ce qui se passe ensuite</h2><p>Un seul interlocuteur qualifié vous accompagne dès le premier rendez-vous.</p></div>
    <div class="steps c3">
      <div class="step s1"><h3>Nous vous contactons</h3><p>Nous revenons vers vous dans les meilleurs délais.</p></div>
      <div class="step s3"><h3>Premier rendez-vous</h3><p>Nous écoutons votre projet et étudions vos besoins.</p></div>
      <div class="step s4"><h3>Devis personnalisé</h3><p>Un devis qui allie vos envies et votre budget.</p></div>
    </div>
  </div>
</section>

<section class="sec mini bg-sage">
  <div class="wrap band">
    <div><h2 style="color:var(--deep)">Partout en Île-de-France sud</h2><p style="color:var(--muted)">Particuliers, entreprises, collectivités et résidences : contrats annuels ou passages ponctuels.</p></div>
    <div class="cta-row"><a class="btn btn-primary" href="savoir-faire.html">Voir nos métiers</a></div>
  </div>
</section>'''
page('contact.html','contact.html','Contact | Albizzia, paysagiste à Angerville (91)','Contactez Albizzia, paysagiste à Angerville : demande de devis par formulaire, téléphone ou e-mail.',ct,'\n<script src="js/contact.js"></script>')
print('ok')
