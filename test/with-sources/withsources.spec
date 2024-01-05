Summary:       Nothing
Name:          withsources
Version:       0.0.0
Release:       1%{?dist}

License:       MIT
URL:           https://github.com/jw3/mock-srpm

Source0:       %{name}.tar.gz

%description
Testing the jw3/mock-srpm GitHub Action

%prep
%autosetup -n %{name}

%build
./build-withsources

%install
install -D %{name} %{buildroot}/%{_bindir}/%{name}

%check

%files
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Fri Jan 05 2024 John Wass <jwass3@gmail.com> 0.0.0-1
- Inception
