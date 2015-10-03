close all; 
lminb=[];
lmaxb=[];
lming=[];
lmaxg=[];
lbmin=zeros(1,5);
lbmax=zeros(1,5);
lgmin=zeros(1,5);
lgmax=zeros(1,5);
k=1;
d=[10,50,100,500,1000];
E=[];
 
for n=[10,50,100,500,1000]
 E=[];
 F=[];
    for i=1:100
        
        ber= 1 - 2*binornd(1,.5,n,n);
        goe=2*randn(n);
        S=eig(ber);
        T=eig(goe);
        
        lminb=[lminb min(S)];
        lmaxb=[lmaxb max(S)];
        lming=[lminb min(T)];
        lmaxg=[lmaxg max(T)];
        
    end
    E= S/sqrt(n);
    F= T/sqrt(n);
       
    lbmin(k)=mean(lminb);
    lbmax(k)=mean(lmaxb);
    lgmin(k)=mean(lming);
    lgmax(k)=mean(lmaxg);
    
     figure(3);
     subplot(2,3,k,'align');
     scatter(real(E),imag(E));
     xlabel('Real Part of the Eigenvalues');
     ylabel('Imaginary Part of the Eigenvaluer');
     %subtitle('Normalized Eigenvalues on complex plane for IID Bernoulli Random Matrix (Asymmetric)');
     
     figure(4);
     subplot(2,3,k,'align');
     scatter(real(F),imag(F));
     xlabel('Real Part of the Eigenvalues');
     ylabel('Imaginary Part of the Eigenvalues');
     %suptitle('Normalized Eigenvalues on complex plane for IID Gaussian Random Matrix (Asymmetric)');
    
     k=k+1;
end
 
figure;
subplot(2,1,1);
scatter(d,lbmin);
xlabel('Dimension of space');
ylabel('Lambda min');
title('Minimum values of Eigenvalues v/s Dimension of space for Bernoulli Asymmetric Matrix');
subplot(2,1,2);
scatter(d,lbmax);
xlabel('Dimension of space');
ylabel('Lambda max');
title('Maximum values of Eigenvalues v/s Dimension of space for Bernoulli Asymmetric Matrix');
%suptitle('Spectral Dependence for IID Bernoulli Asymmetric Matrix');
 
figure;
subplot(2,1,1);
scatter(d,lgmin);
xlabel('Dimension of space');
ylabel('Lambda min');
title('Minimum values of Eigenvalues v/s Dimension of space for Gaussian Asymmetric Matrix');
subplot(2,1,2);
scatter(d,lgmax);
xlabel('Dimension of space');
ylabel('Lambda max');
title('Maximum values of Eigenvalues v/s Dimension of space for Gaussian Asymmetric Matrix');
%suptitle('Spectral Dependence for IID Gaussian Asymmetric Matrix');
