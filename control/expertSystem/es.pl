% LOGIC FROM https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/children.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fprepare%2Fchildren.html
% https://www.cdc.gov/coronavirus/2019-nCoV/hcp/clinical-criteria.html


%  Tell prolog that known/3 will be added later by asserta
:- dynamic known/3.

% _____ KB _____
action(call_emergency_services) :- symptoms(severe).
action(ensure_optimal_care_and_prevent_nosocomial_infections) :- priority(level1).
action(test_and_care_urgently) :- priority(level2).
action(test_and_care_as_resources_allow) :- priority(level3).
action(stay_at_home_and_monitor) :- priority(level4).


priority(level1) :- work(healthcare_worker), symptoms(low).
priority(level1) :- work(healthcare_worker), symptoms(mild).

priority(level1) :- currently_hospitalised(present), symptoms(low).
priority(level1) :- currently_hospitalised(present), symptoms(mild).

priority(level2) :- vulnerability(high), symptoms(low).
priority(level2) :- vulnerability(high), symptoms(mild).
priority(level2) :- work(first_responder), symptoms(low).
priority(level2) :- work(first_responder), symptoms(mild).

priority(level3) :- symptoms(mild), exposure(likely).

priority(level4) :- age(under_18), symptoms(mild).
%priority(level4) :- age(under_18), symptoms(low).

vulnerability(low) :- age(under_18).
% vulnerability(mid) :- age(between_18_and_64).
vulnerability(high) :- age(above_65).
vulnerability(high) :- preexisting_condition(present).


symptoms(severe) :- chest(in_pain).
symptoms(severe) :- breathing(difficult).
symptoms(severe) :- disorientation(present).
symptoms(mild) :- fever(present).
symptoms(mild) :- chills(present).
symptoms(mild) :- sweating(present).
symptoms(mild) :- chest(tight). % haha english
symptoms(mild) :- cough(present).
symptoms(mild) :- sore_throat(present).
symptoms(mild) :- body_aches(present).
symptoms(mild) :- vomiting(present).
symptoms(low) :- diarrhoea(present).
symptoms(low) :- fatigue(present).
symptoms(low) :- smell(lost).
symptoms(low) :- nose(runny).
symptoms(low) :- throat(sore).
symptoms(low) :- lips(bluish).
symptoms(low) :- face(bluish).
symptoms(mild) :- \+arousal(possible).

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
diarrhoea(X) :- ask(diarrhoea,X).
pressure(X) :- ask(pressure, X).
vomiting(X) :- ask(vomiting, X).
fatigue(X) :- ask(fatigue, X).
smell(X) :- ask(smell, X).
nose(X) :- ask(nose, X).
throat(X) :- ask(throat, X).
lips(X) :- ask(lips, X).
face(X) :- ask(face, X).
arousal(X) :- ask(arousal, X).

% Pre-existing conditions
asthma(X) :- ask(asthma,X).
lung_disease(X) :- ask(lung_disease,X).
cancer(X) :- ask(cancer,X).
immunosuppressed(X) :- ask(immunosuppressed,X).
heart_conditions(X) :- ask(heart_conditions,X).
pregnancy(X) :- ask(pregnancy,X).

% Exposure and Spread
last_international_travel(X) :- ask(last_international_travel,X).
last_visit_to_COVID_infected_area(X) :- ask(last_visit_to_COVID_infected_area,X).
work(X) :- ask(work,X).
currently_hospitalised(X) :- ask(currently_hospitalised,X).

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
