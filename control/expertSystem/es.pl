% LOGIC FROM https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/children.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fprepare%2Fchildren.html
% https://www.cdc.gov/coronavirus/2019-nCoV/hcp/clinical-criteria.html


%  Tell prolog that known/3 will be added later by asserta
:- dynamic known/3.

% _____ KB _____
action(call_emergency_services) :- symptoms(severe).
action(contact_hospital_and_prevent_nosocomial_infections) :- priority(level1).
action(contact_hospital_for_testing_and_care) :- priority(level2).
action(ask_heathcare_provider_about_testing) :- priority(level3).

symptoms(severe) :- chest(in_pain).
symptoms(severe) :- breathing(difficult).
symptoms(severe) :- disorientation(present).

% TO DO: if kiddo is sick, isolate but deal with mental health as well
% under 18 and sick, stay at home and isolate
% If others in your home are at particularly high risk for severe illness from COVID-19, consider extra precautions to separate your child from those people.
% If you are unable to stay home with your child while school is out, carefully consider who might be best positioned to provide child care. If someone at higher risk for COVID-19 will be providing care (older adult, such as a grandparent or someone with a chronic medical condition), limit your children’s contact with other people.
% Consider postponing visits or trip to see older family members and grandparents. Connect virtually or by writing letters and sending via mail.

%priority(level3) :- symptoms(mild), exposure(likely).

vulnerability(low) :- age(under_18).
vulnerability(mid) :- age(between_18_and_64).
vulnerability(high) :- age(above_65).
vulnerability(high) :- preexisting_condition(present).

symptoms(mild) :- fever(present).
symptoms(mild) :- chills(present).
symptoms(mild) :- sweating(present).
symptoms(mild) :- chest(uncomfortable). % haha english
symptoms(mild) :- cough(present).
symptoms(mild) :- sore_throat(present).
symptoms(mild) :- body_aches(present).
symptoms(mild) :- vommiting(present).
symptoms(mild) :- diarrhoea(present).

exposure(likely) :- last_international_travel(under_14_days_ago). % ugh english
exposure(likely) :- last_visit_to_COVID_infected_area(under_14_days_ago). % ugh english
exposure(likely) :- work(in_a_medical_facility). % ugh english

preexisting_condition(X) :- asthma(X). % match value (present)
preexisting_condition(X) :- lung_disease(X).
preexisting_condition(X) :- cancer(X).
preexisting_condition(X) :- immunosuppressed(X).
preexisting_condition(X) :- heart_conditions(X).
preexisting_condition(X) :- pregnancy(X).

% _____ ASKABLES _____

% Emergency
chest(X) :- ask(chest,X).
breathing(X) :- ask(breathing,X).
disorientation(X) :- ask(disorientation,X).

% Vulnerability
age(X) :- ask(age,X).

% Symptoms
fever(X) :- ask(fever,X).
chills(X) :- ask(chills,X).
sweating(X) :- ask(sweating,X).
chest(X) :- ask(chest,X).
cough(X) :- ask(cough,X).
sore_throat(X) :- ask(sore_throat,X).
body_aches(X) :- ask(body_aches,X).
vommiting(X) :- ask(vommiting,X).
diarrhoea(X) :- ask(diarrhoea,X).

% Preesisting condition
asthma(X) :- ask(asthma,X).
lung_disease(X) :- ask(lung_disease,X).
cancer(X) :- ask(cancer,X).
immunosuppressed(X) :- ask(immunosuppressed,X).
heart_conditions(X) :- ask(heart_conditions,X).
pregnancy(X) :- ask(pregnancy,X).
% TO DO: add more

% Exposure
last_international_travel(X) :- ask(last_international_travel,X).
last_visit_to_COVID_infected_area(X) :- ask(last_visit_to_COVID_infected_area,X).
work(X) :- ask(work,X).

% _____ ASKING LOGIC _____
% Asking clauses
multivalued(none). % We don't have any multivalued attributes

ask(A, V):-
known(yes, A, V), % succeed if true
!.	% stop looking

ask(A, V):-
known(_, A, V), % fail if false
!, fail.

% If not multivalued, and already known, don't ask again for a different value.
ask(A, V):-
\+multivalued(A),
known(yes, A, V2),
V \== V2,
!.

ask(A, V):-
read_py(A,V,Y), % get the answer
asserta(known(Y, A, V)), % remember it
write_py(known(Y, A, V)),
Y == yes.	% succeed or fail
