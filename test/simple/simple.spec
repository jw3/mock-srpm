Summary:       Nothing
Name:          simple
Version:       0.0.0
Release:       1%{?dist}

License:       MIT
URL:           https://github.com/jw3/mock-srpm

%description
Testing the jw3/mock-srpm GitHub Action

%prep

%build
echo "echo %{version}" > %{name}

%install
install -D %{name} %{buildroot}/%{_bindir}/%{name}

%check

%files
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Tue Dec 12 2023 John Wass <jwass3@gmail.com> 0.0.0-1
- Inception
