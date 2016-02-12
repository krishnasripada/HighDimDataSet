function [ adjMatrix, partition] = AdjacencyMatrix(p,q,n)
I = eye(n);
ix = randperm (n);
T = I(ix,:);
n2 = n/2;
P = random('bino', 1, p, n2, n2); % upper left block
dP2 = random('bino', 1, p, n2, 1); % diagonal of the lower right block
Q = random('bino', 1, q, n2, n2); % upper right block
% carve the two triangular and diagonal matrices that we need
U = triu(P, 1);
L = tril(P,-1);
dP = diag(P);
A0 = U + U' + diag(dP);
A1 = Q;
A2 = Q';
A3 = L + L' + diag(dP2);
A =[A0 A1;A2 A3];
adjMatrix = T*A*T.';
[V,D] = eig(adjMatrix);
secondDEVT = V(:,n-1);
for i=1:numel(secondDEVT)
    element = abs(secondDEVT(i));
    if element+1 ~=1
        partition(i) = 1;
    else
        partition(i) = -1;
    end
end
end

