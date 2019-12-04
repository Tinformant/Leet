## Computer Set 4
### Question 1
For PDF or CDF is about the probability of random variables within a certain range. It is meaningless to analyze a critical condition. 

### Question 2
```matlab
Num Data = 250000; 
I0 = 1; 
V0 = 1;

Data R = rand(Num Data,1) + 1;
Data C = 3.5 * rand(Num Data,1) + 1.5;
Data L = exprnd(2,[Num Data,1]) + 1;

Data alpha = Data R./(2.*Data L);
Data omega = 1./sqrt(Data C.*Data L);

Data = Data alpha - Data omega;
Data(Data<0)=0; % underdamped
Data(Data>0)=1; % overdamped

fprintf('the probability of overdamped system is %fnn', sum(Data)/Num Data);
fprintf('the probability of underdamped system is %fnn', (Num Data-sum(Data))/Num Data);
```

### Question 3
Code
```matlab
S1 = -Data_alpha(Data == 1) + sqrt(Data_alpha(Data == 1).^2 - Data_omega(Data == 1).^2);
S2 = -Data_alpha(Data == 1) - sqrt(Data_alpha(Data == 1).^2 - Data_omega(Data == 1).^2);

L = Data_L(Data == 1); 
R = Data_R(Data == 1); 
A = zeros(2,length(S1));

for i_t = 1:length(S1)
    A(:,i_t) = [1,1;S1(i_t,1),S2(i_t,1)]\[I0; -1/L(i_t,1)*(R(i_t,1)*I0+V0)];
end

A1 = A(:,1); 
A2 = A(:,2); 

[pS1,cS1,xS1] = pcdf(S1,50,max(S1)+0.1*(max(S1)-min(S1)),min(S1)-0.1*(max(S1)-min(S1)));
[pS2,cS2,xS2] = pcdf(S2,50,max(S2)+0.1*(max(S2)-min(S2)),min(S2)-0.1*(max(S2)-min(S2)));
[pA1,cA1,xA1] = pcdf(A1,50,0,-10);
[pA2,cA2,xA2] = pcdf(A2,50,10,0);

f(1,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xS1,pS1,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xS1,cS1,'--o','LineWidth',1.5);
title({'Given a overdamped system, margin PDF and CDF of S1';' '});legend('pdf','cdf','Location','northwest');

f(2,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xS2,pS2,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xS2,cS2,'--o','LineWidth',1.5);
title({'Given a overdamped system, margin PDF and CDF of S2';' '});legend('pdf','cdf','Location','northwest');

f(3,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xA1,pA1,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xA1,cA1,'--o','LineWidth',1.5);
title({'Given a overdamped system, margin PDF and CDF of A1';' '});legend('pdf','cdf','Location','northwest');

f(4,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xA2,pA2,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xA2,cA2,'--o','LineWidth',1.5);
title({'Given a overdamped system, margin PDF and CDF of A2';' '});legend('pdf','cdf','Location','northwest');
```

### Question 5
```matlab
% PDF of t = 1s
t = 1;
i_over = A1.*exp(S1*t) + A2.*exp(S2*t);
i_under = exp(-Data_alpha(Data == 0)*t).*(AA1.*cos(omega_D*t)+AA2.*sin(omega_D*t));
i_t = [i_over;i_under];
[pI,cI,xI] = pcdf(i_t,50,max(i_t)+0.1*(max(i_t)-min(i_t)),min(i_t)-0.1*(max(i_t)-min(i_t)));

f(8,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xI,pI,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xI,cI,'--o','LineWidth',1.5);
title({'Given t = 1s, PDF and CDF of i(s)';' '});legend('pdf','cdf','Location','northwest');
```
