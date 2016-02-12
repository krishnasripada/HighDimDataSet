function [community1, community2] = partition(adjMatrix)
[V,D] = eig(adjMatrix);
[X,Y] = sort(max(abs(D)), 'descend');
secondDEVR = V(:,Y(2));
community1=[];
community2=[];
for i=1:numel(secondDEVR)
    element = secondDEVR(i);
    if element>0
        community1(i)=1;
    else
        community2(i)=1;
    end
end
end

